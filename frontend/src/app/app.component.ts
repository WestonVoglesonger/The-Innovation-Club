import { Component, OnInit } from "@angular/core";
import { Router } from "@angular/router";

@Component({
  selector: "app-root",
  template: `
    <app-navigation></app-navigation>
    <router-outlet></router-outlet>
  `,
})
export class AppComponent implements OnInit {
  title = "frontend";
  constructor(private router: Router) {}

  ngOnInit() {
    document.addEventListener("keydown", (event) => {
      if (event.ctrlKey && event.shiftKey && event.key === "A") {
        this.router.navigate(["/admin"]);
      }
    });
  }
}
