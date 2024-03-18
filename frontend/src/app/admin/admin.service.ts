import { Injectable } from "@angular/core";
import {
  Observable,
  OperatorFunction,
  ReplaySubject,
  catchError,
  map,
  throwError,
} from "rxjs";
import { HttpClient } from "@angular/common/http";
import { AdminData } from "./admindata";

@Injectable({
  providedIn: "root",
})
export class AdminService {
  private admins: ReplaySubject<AdminData[]> = new ReplaySubject(1);
  admins$: Observable<AdminData[]> = this.admins.asObservable();

  constructor(protected http: HttpClient) {
    // Sets the initial value of the admins replay subject to an empty list of admins.
    // This way, we can always guarantee that the next value from `admins$` will never be null.
    this.admins.next([]);
  }

  /** Refreshes the internal `admins$` observable with the latest admin data from the API. */
  getAdmins() {
    return this.http
      .get<AdminData[]>("/api/admin")
      .subscribe((timers) => this.admins.next(timers));
  }

  /** Returns a single admin from the API as an observable.  */
  getAdmin(id: number): Observable<AdminData> {
    return this.http.get<AdminData>("/api/admin/" + id);
  }

  /** Creates a new admin and returns the created admin from the API as an observable. */
  createAdmin(request: AdminData): Observable<AdminData> {
    return this.http.post<AdminData>("/api/admin", request).pipe(
      catchError((error) => {
        // Handle specific error status codes or messages as needed
        if (error.status === 405) {
          // Example: Handle adminRegistrationException
          alert("Registration error: email is already registered.");
        }
        // Re-throw the error for further handling if needed
        return throwError(() => new Error("Registration failed"));
      }),
    );
  }

  /** Edits a admin and returns the edited admin from the API as an observable. */
  editAdmin(request: AdminData): Observable<AdminData> {
    return this.http.put<AdminData>("/api/admin", request);
  }

  /** Deletes a admin and returns the delete action as an observable. */
  deleteAdmin(id: number) {
    return this.http.delete("/api/admin/" + id);
  }

  /** Checks if the email is already registered and returns a boolean value as an observable. */
  checkEmailIsRegistered(email: string): Observable<boolean> {
    return this.http.get<boolean>(`/api/check-email/${email}`);
  }
}
