import { Component } from '@angular/core';
import {Login} from "./models/login";
import { Router, NavigationEnd } from '@angular/router';
import { AuthService } from './http.service';
import { Observable } from 'rxjs/Observable';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor(private router: Router,
              private auth:AuthService) {
  }
  ngOnInit() {
  }
}
