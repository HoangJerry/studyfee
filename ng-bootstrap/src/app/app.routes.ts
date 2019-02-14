import {HomeComponent} from "./pages/home/home.component";
import {LoginComponent} from "./pages/login/login.component";
import {StudentsComponent} from "./pages/students/students.component";
import { AuthGuard } from './http.service';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { BrowserModule } from '@angular/platform-browser';

import { BaseLayoutComponent } from './base-layout/base-layout.component';

import { SiteLayoutComponent } from './site-layout/site-layout.component';

const routes=[
    {
        path:'',
        component: BaseLayoutComponent,
        children: [
            {
                path: 'login',
                component: LoginComponent
            }
        ]
    },
    {
        path: '',
        component: SiteLayoutComponent,
        children: [
            {
                path: 'students',
                component: StudentsComponent,
                canActivate:[AuthGuard]
            },
            {
                path: 'home',
                component: HomeComponent,
                canActivate:[AuthGuard]
            },
            {
                path: 'others',
                loadChildren:'./pages/others/others.module#OthersModule',
            },
        ]
    },
    {
        path: '**',
        redirectTo:'/students',
    }
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
