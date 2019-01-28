import {HomeComponent} from "./pages/home/home.component";
import {LoginComponent} from "./pages/login/login.component";
import {StudentsComponent} from "./pages/students/students.component";
import { AuthGuard } from './http.service';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

const routes=[
    {
        path:'',
        redirectTo:'/students',
        pathMatch:'full'
    },
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
        path: 'login',
        component: LoginComponent
    },
    {
        path: 'others',
        loadChildren:'./pages/others/others.module#OthersModule',
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
