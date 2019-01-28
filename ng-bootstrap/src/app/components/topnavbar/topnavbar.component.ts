import { Component, Input } from '@angular/core';
import {smoothlyMenu} from "../../app.helpers";
import {Login} from "../../models/login";
import { Router }                   from '@angular/router'

@Component({
    selector: 'topnavbar',
    templateUrl: 'topnavbar.component.html'
})
export class Topnavbar {
    loginInfo :any;
    constructor(private router: Router) {
        this.loginInfo = JSON.parse(localStorage.getItem('user'));
    }
    ngOnInit() {

    }
    toggleNavigation(): void {
        jQuery("body").toggleClass("mini-navbar");
        smoothlyMenu();
    }
    logout() {
        localStorage.clear();
        this.router.navigate(['/login']);
    }
}