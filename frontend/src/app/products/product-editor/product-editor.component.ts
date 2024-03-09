import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ProductService } from '../products.service';
import { FormBuilder, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-product-editor',
  templateUrl: './product-editor.component.html',
  styleUrls: ['./product-editor.component.css']
})
export class ProductEditorComponent {
  /** Form controls (individual form items) */
  name = new FormControl('', [Validators.required, Validators.maxLength(50)]); // Limit to 50 characters
  description = new FormControl('', [Validators.required, Validators.maxLength(100)]); // Limit to 200 characters
  url = new FormControl('', [Validators.required]); // No length limit

  /** Form group (stores all form controls) */
  public productForm = this.formBuilder.group({
    name: this.name,
    description: this.description,
    url: this.url,
  });

  /** Stores the ID of the product currently being edited. */
  id: number = -1;

  /** Stores whether or not the product is new. */
  isNew: boolean = false;

  constructor(
    private productService: ProductService,
    private route: ActivatedRoute,
    protected formBuilder: FormBuilder,
    private router: Router,
  ) {
    // Determine if the product is new.
    this.isNew = route.snapshot.params['product_id'] == 'new';

    // If the product is not new, set existing product data and update the forms.
    if (!this.isNew) {
      this.id = route.snapshot.params['product_id'];
      productService.getProduct(this.id).subscribe((productData) => {
        this.productForm.setValue({
          name: productData.name,
          description: productData.description,
          url: productData.url,
        });
      });
    }
  }

  /** Function that runs when the form is submitted. */
  public onSubmitForm() {
    // First, ensure that the form is valid (all validators pass). Otherwise, display a snackbar error.
    if (this.productForm.valid) {
      // If the product is new, create it.
      if (this.isNew) {
        this.productService
          .createProduct({
            id: null,
            name: this.name.value ?? '',
            description: this.description.value ?? '',
            url: this.url.value ?? '',
          })
          .subscribe((_) => {
            // Navigate back to the products page once the operation is complete.
            this.router.navigate(['/products']);
          });
      } else {
        this.productService
          .editProduct({
            id: this.id,
            name: this.name.value ?? '',
            description: this.description.value ?? '',
            url: this.url.value ?? '',
          })
          .subscribe((_) => {
            // Navigate back to the products page once the operation is complete.
            this.router.navigate(['/products']);
          });
      }
    } 
  }
}
