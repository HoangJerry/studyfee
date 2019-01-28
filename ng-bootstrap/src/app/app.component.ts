import { Component } from '@angular/core';
import {Login} from "./models/login";
import { Router, NavigationEnd } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  loginInfo:Login = {
      first_name:'Andrew',
      last_name:'Yang',
      avatar:'ay.jpeg',
      title:'Senior Developer'
  };

  currentUrl: string='';

  constructor(private router: Router) {
  	this.router.events.subscribe((e) => {
	  if (e instanceof NavigationEnd) {
	    this.currentUrl = e.url;
	  }
	});
  }
  
}
