import { Component, OnInit } from '@angular/core';
import { HttpService, AuthService } from '../../http.service';
import { Router }                   from '@angular/router'
import { ToastyService, ToastyConfig, ToastOptions, ToastData } from 'ng2-toasty';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
	email:any;
	password:any;
  constructor(private http: HttpService,
  					private toastyService:ToastyService,
  					private router: Router,
            private auth:AuthService) {
  	
  }

  ngOnInit() {
    // this.auth.isLoggedIn().then((a)=>{console.log(a)})
    this.auth.hasToken().subscribe((result)=>{
      // console.log(result);
      if (result){
        // this.router.navigate(['/home']);
        window.location.href='/home';
      }
    })
        // this.router.navigate(['/home']);
        // console.log("ch")
        // window.location.href='/home';
     
  }

  onClickLogin = () =>{
  	this.http.UserLogin(this.email,this.password).subscribe(
      (data:any) => {
        localStorage.setItem('user',JSON.stringify(data));
        this.auth.login(data.auth_token)
        this.toastyService.success("Login success!");
        // this.router.navigate(['/home']);
        window.location.href='/home';
      },
      (error)=>{
        this.toastyService.error(error.error.detail);
      }
    );
  }

}
