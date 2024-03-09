import { Component, Input } from "@angular/core";
import { ProductService } from "../products.service";
import { ProductData } from "../productdata";
import { Router } from "@angular/router";

@Component({
  selector: "product-widget",
  templateUrl: "./product.widget.html",
  styleUrls: ["./product.widget.css"],
})
export class ProductWidget {
  /** Product this widget is showing. */
  @Input() productData!: ProductData;

  // Modify the constructor to inject the ProductService
constructor(
  public productService: ProductService,
  public router: Router
) {}

// Add a new method to fetch the screenshot
getScreenshotUrl() {
  return this.productService.getScreenshotUrl(this.productData.url);
}

  /** Navigates to the product edit page */
  editProduct() {
    this.router.navigate(["/products/edit", this.productData.id]);
  }

  /** Deletes the current product */
  deleteProduct() {
    this.productService.deleteProduct(this.productData.id!).subscribe(() => {
      // Subscribe to the getProducts() method to refresh the product list
      this.productService.getProducts().subscribe();
    });
  }
}  