import { Component, OnInit } from "@angular/core";
import { Router } from "@angular/router";
import { ProductService } from "./products.service";
import { ProductData } from "./productdata"; // Update the import path as needed

@Component({
  selector: "app-products",
  templateUrl: "./products.component.html",
  styleUrls: ["./products.component.css"],
})
export class ProductsComponent implements OnInit {

  products: ProductData[] = [];

  constructor(
    public router: Router,
    public productService: ProductService,
  ) {}

  ngOnInit(): void {
    this.productService.getProducts().subscribe((products) => {
      this.products = products;
    });
  }

  navigateToCreateProduct() {
    this.router.navigate(['products/edit/new']);
  }
}
