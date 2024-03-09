import { Injectable } from "@angular/core";
import { Observable, ReplaySubject, throwError } from "rxjs";
import { HttpClient } from "@angular/common/http";
import { ProductData } from "./productdata";
import { catchError, map } from "rxjs/operators";

@Injectable({
  providedIn: "root",
})
export class ProductService {
  private products: ReplaySubject<ProductData[]> = new ReplaySubject(1);
  products$: Observable<ProductData[]> = this.products.asObservable();
  private apiKey = '02ca0b1d857da21a9d7b85c42a407cc4';
  private screenshotApiUrl = 'https://api.screenshotlayer.com/api/capture?access_key=02ca0b1d857da21a9d7b85c42a407cc4';

  constructor(protected http: HttpClient) {
    this.products.next([]);
  }

  getProducts(): Observable<ProductData[]> {
    return this.http.get<ProductData[]>("/api/product").pipe(
      catchError((error) => {
        // Handle errors as needed
        return throwError(() => new Error("Failed to fetch products"));
      }),
      map((products) => {
        this.products.next(products);
        return products;
      }),
    );
  }

  getProduct(id: number): Observable<ProductData> {
    return this.http.get<ProductData>("/api/product/" + id);
  }

  createProduct(request: ProductData): Observable<ProductData> {
    return this.http.post<ProductData>("/api/product", request).pipe(
      catchError((error) => {
        if (error.status === 406) {
          alert("Registration error: product is already registered.");
        }
        return throwError(() => new Error("Registration failed"));
      }),
    );
  }

  editProduct(request: ProductData): Observable<ProductData> {
    return this.http.put<ProductData>("/api/product", request);
  }

  deleteProduct(id: number): Observable<void> {
    return this.http.delete<void>("/api/product/" + id);
  }

  getScreenshotUrl(webpageUrl: string): string {
    return `${this.screenshotApiUrl}&url=${encodeURIComponent(webpageUrl)}`;
  }  
}