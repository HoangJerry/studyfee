import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { HttpClientModule } from '@angular/common/http'

import { AppComponent } from './app.component';
import { Topnavbar } from "./components/topnavbar/topnavbar.component";
import { Navigation } from "./components/navigation/navigation.component";
import { RouterModule } from "@angular/router";
import { AppRoutingModule } from "./app.routes";
import { HomeComponent } from "./pages/home/home.component";
import { LoginComponent } from './pages/login/login.component';
import { StudentsComponent } from './pages/students/students.component';

import { HttpService, AuthService, AuthGuard } from './http.service';
import { ToastyModule } from 'ng2-toasty';
import { ModalModule } from "ngx-modal";
import { BaseLayoutComponent } from './base-layout/base-layout.component';
import { SiteLayoutComponent } from './site-layout/site-layout.component';
@NgModule({
  declarations: [
    AppComponent,
    Navigation,
    Topnavbar,
    HomeComponent,
    LoginComponent,
    StudentsComponent,
    BaseLayoutComponent,
    SiteLayoutComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    HttpModule,
    AppRoutingModule,
    ToastyModule.forRoot(),
    ModalModule,
  ],
  providers: [HttpService, AuthService, AuthGuard],
  bootstrap: [AppComponent]
})
export class AppModule { }
