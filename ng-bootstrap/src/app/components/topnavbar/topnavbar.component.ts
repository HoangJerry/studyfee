import { Component, Input } from '@angular/core';
import {smoothlyMenu} from "../../app.helpers";
import {Login} from "../../models/login";

@Component({
    selector: 'topnavbar',
    templateUrl: 'topnavbar.component.html'
})
export class Topnavbar {
    @Input() loginInfo:Login;
    ngOnInit() {

    }
    toggleNavigation(): void {
        jQuery("body").toggleClass("mini-navbar");
        smoothlyMenu();
    }
    logout() {
        localStorage.clear();
        // location.href='http://to_login_page';
    }
}