import { Injectable } from '@angular/core';
import { RequestOptions } from '@angular/http';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { CanActivate, Router, ActivatedRouteSnapshot, RouterStateSnapshot }              from '@angular/router';
import { BehaviorSubject, Observable } from 'rxjs';
import { ToastyService, ToastyConfig, ToastOptions, ToastData } from 'ng2-toasty';


@Injectable()
export class HttpService {
  APIURL = 'http://localhost:8000/api/'
  headers:HttpHeaders = new HttpHeaders;
  constructor(private http: HttpClient) {
  	this.headers = this.headers.set('Content-Type', 'application/json; charset=utf-8');
  }

  UserLogin = (account?,password?,token?) => {
  	// account = account.toString('hex');
    if (token){
      let headers = this.headers
      headers = headers.set('Authorization','Token '+token)
      return this.http.post(this.APIURL+'user/me/',{},{headers:headers});
    }
    else{
      let data = {
        'email':account,
        'password':password
      }
      return this.http.post(this.APIURL+'user/me/',data);
    }
  }

  StudentList = (page?) => {
    let headers = this.headers
    headers = headers.set('Authorization','Token '+localStorage.getItem('token'))
    return this.http.get(this.APIURL+'student/?offset='+page,{headers:headers})
  }
  ClassList = () => {
    let headers = this.headers
    headers = headers.set('Authorization','Token '+localStorage.getItem('token'))
    return this.http.get(this.APIURL+'class/',{headers:headers})
  }
  SchoolList = () => {
    let headers = this.headers
    headers = headers.set('Authorization','Token '+localStorage.getItem('token'))
    return this.http.get(this.APIURL+'school/',{headers:headers})
  }

  StudentCreate = (data) => {
    let headers = this.headers
    headers = headers.set('Authorization','Token '+localStorage.getItem('token'))
    return this.http.post(this.APIURL+'student/',data,{headers:headers})
  }

  StudentUpdate = (data) => {
    let pk = data.id
    let headers = this.headers
    headers = headers.set('Authorization','Token '+localStorage.getItem('token'))
    return this.http.put(this.APIURL+'student/'+pk+'/',data,{headers:headers})
  }

  StudentDeleteList = (list_delete) => {

    let data = {
      "list_delete" : list_delete
    }
    let headers = this.headers;
    headers = headers.set('Authorization','Token '+ localStorage.getItem('token'))
    return this.http.post(this.APIURL+'student/',data,{headers:headers})
  }

  StudentDelete = (pk) => {
    let headers = this.headers;
    headers = headers.set('Authorization','Token '+ localStorage.getItem('token'))
    return this.http.delete(this.APIURL+'student/'+pk+'/',{headers:headers})
  }

}

@Injectable()
export class AuthService {
    constructor(private http: HttpService, private toastyService: ToastyService,
        private toastyConfig: ToastyConfig, private router: Router) {
        this.toastyConfig.theme = 'material';
    }

    isLoginSubject: boolean = false;
    async isLoggedIn() {
        await this.hasToken();
        return this.isLoginSubject;
    }

    login(token): void {
        localStorage.setItem('token', token);
        this.isLoginSubject = true;
    }

    logout = () => {
        localStorage.removeItem('token');
        this.isLoginSubject = false;
        localStorage.removeItem('body');
    }

 
    hasToken(): Observable < boolean > {
        return new Observable(observer => {
                if (!localStorage.getItem('token')) {
                    this.isLoginSubject = false;
                    this.router.navigate(['/login']);
                    observer.next(false);
                    observer.complete();
                } else {
                    this.http.UserLogin(null, null, localStorage.getItem('token'))
                        .subscribe(
                            (data: any) => {
                                localStorage.setItem('user',JSON.stringify(data));
                                this.isLoginSubject = true;
                                observer.next(true);
                                observer.complete();
                            },
                            (error) => {
                                this.toastyService.error(error.error.detail);
                                this.isLoginSubject = false;
                                this.router.navigate(['/login']);
                                observer.next(false);
                                observer.complete();
                            })
                }
            })
      } 
}
@Injectable()
export class AuthGuard implements CanActivate {
    constructor(private router: Router, private _auth:AuthService) { }

    canActivate(next:ActivatedRouteSnapshot, state:RouterStateSnapshot): Observable<boolean> {
        // not logged in so redirect to login page with the return url
        return this._auth.hasToken();
        
        
    }
}

// @Injectable()
// export class AuthService {
//     constructor(private http: HttpService, private toastyService: ToastyService,
//         private toastyConfig: ToastyConfig, private router: Router) {
//         this.toastyConfig.theme = 'material';
//     }

//     isLoginSubject: boolean = false;
//     isLoggedIn() {
//         console.log(localStorage.getItem('token'));
//         if (localStorage.getItem('token')!=null){ return true};
//         return false;
//     }

//     login(token): void {
//         localStorage.setItem('token', token);
//         this.isLoginSubject = true;
//     }

//     logout = () => {
//         localStorage.removeItem('token');
//         this.isLoginSubject = false;
//         localStorage.removeItem('body');
//     }
// }
// @Injectable()
// export class AuthGuard implements CanActivate {
//     constructor(private router: Router, private _auth:AuthService) { }

//     canActivate(next:ActivatedRouteSnapshot, state:RouterStateSnapshot): boolean {
//         // not logged in so redirect to login page with the return url
//         if (this._auth.isLoggedIn()) return true;   
//         this.router.navigate(['/login']);
//         return false;       
//     }
// }
