import { Component, OnInit } from "@angular/core";
import { FormBuilder, FormGroup, Validators } from "@angular/forms";
import { AdminService } from "./admin.service";
import { AdminData } from "./admindata";

@Component({
  selector: "app-admin",
  templateUrl: "./admin.component.html",
  styleUrls: ["./admin.component.css"],
})
export class AdminComponent implements OnInit {
  adminForm!: FormGroup;
  isEmailRegistered: boolean = false;

  constructor(
    private fb: FormBuilder,
    public adminService: AdminService,
  ) {}

  ngOnInit(): void {
    this.adminForm = this.fb.group({
      firstName: ["", Validators.required],
      lastName: ["", Validators.required],
      email: ["", [Validators.required, Validators.email]],
      password: ["", [Validators.required, Validators.minLength(8)]],
      accessCode: ["", Validators.required],
    });

    this.adminForm.get("email")?.valueChanges.subscribe((value) => {
      this.checkEmailIsRegistered(value);
    });
  }

  checkEmailIsRegistered(email: string) {
    this.adminService
      .checkEmailIsRegistered(email)
      .subscribe((isRegistered) => {
        this.isEmailRegistered = isRegistered;
      });
  }

  onSubmit(): void {
    if (this.adminForm.valid) {
      console.log("Form Submitted:", this.adminForm.value);

      // Validate the access code first
      const accessCode = this.adminForm.value.accessCode;
      this.adminService.validateAccessCode(accessCode).subscribe({
        next: (isValidCode) => {
          if (isValidCode) {
            this.adminService
              .createAdmin({
                first_name: this.adminForm.value.firstName,
                last_name: this.adminForm.value.lastName,
                email: this.adminForm.value.email,
                password: this.adminForm.value.password,
              })
              .subscribe({
                next: (admin: AdminData) => {
                  alert("Admin created successfully.");
                },
                error: () => {
                  alert("Failed to create admin.");
                },
              });
          } else {
            alert("Invalid access code. Please try again.");
          }
        },
        error: () => {
          alert("Error validating access code.");
        },
      });
    } else {
      if (this.isEmailRegistered) {
        alert("Email is already registered.");
      } else {
        alert("Please fill out the form correctly.");
      }
    }
  }
}
