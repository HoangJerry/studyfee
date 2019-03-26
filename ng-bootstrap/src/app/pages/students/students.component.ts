import { Component, OnInit } from '@angular/core';
import { HttpService } from '../../http.service';
import { ToastyService, ToastyConfig, ToastOptions, ToastData } from 'ng2-toasty';
import { Stutdent } from '../../models/student'


declare var $: any;

@Component({
  selector: 'app-students',
  templateUrl: './students.component.html',
  styleUrls: ['./students.component.css']
})
export class StudentsComponent implements OnInit {
  students :any;
  selected:any;
  search:any = {'study_at_class':"",'school':""};
  preBtn:any;
  nextBtn:any;
  currentPage:any = 1;
  pages:any;
  numberPerPage:number = 10;
  new_student:Stutdent = new Stutdent;
  multiSelect:any = false;
  onSearching:any = false;
  multiSelectedList = [];
  selectClass:any;
  selectSchool:any;
  selectGender:any = [{"value":"0","name":"Nam"},
                  {"value":"10","name":"Nữ"},
                  {"value":"20","name":"Không xác định"},]

  constructor(private http:HttpService,
            private toastyService:ToastyService) {
    console.log(this.new_student);
  	this.getStudents((this.currentPage-1)*this.numberPerPage);
    this.http.ClassList().subscribe((data)=>{
      this.selectClass=data;
    })
    this.http.SchoolList().subscribe((data)=>{
      this.selectSchool=data;
      console.log(this.selectSchool);
    })
  }

  ngOnInit() {

  }
  inMulti = (student) =>{
    if (this.multiSelectedList.indexOf(student)>-1){
      return true
    }
    return false
  }

  turnOffMultiSelect = () =>{
    this.multiSelect = false;
    this.multiSelectedList = [];
  }

  onClickRow = (student) => {
    if (this.multiSelect==false){
      this.selected = student
    }
    else{
      this.selected = null;
      let index =this.multiSelectedList.indexOf(student);
      if (index >-1){
        this.multiSelectedList.splice(index, 1);
        if (this.multiSelectedList.length==0){
          this.multiSelect=false;
        }
      }
      else{
        this.multiSelectedList.push(student);
      }
    }
  }

  getStudents = (page?,search?) => {
    this.http.StudentList(page,search).subscribe((data:any)=>{
      this.students=data.results;
      this.preBtn = data.previous;
      this.nextBtn = data.next;
      let pages;
      if (parseInt(data.count)%this.numberPerPage){
        pages = Math.floor(parseInt(data.count)/this.numberPerPage)+1
      }
      else{
        pages = Math.floor(parseInt(data.count)/this.numberPerPage)
      }
      this.pages = Array.from(new Array(pages),(val,index)=>index+1);
    },
    (error)=>{
        this.toastyService.error(error.error.detail);
    })
  } 

  onClickDelete = () => {
    if (this.selected) {
      this.http.StudentDelete(this.selected.id).subscribe((data)=>{
        this.getStudents((this.currentPage-1)*this.numberPerPage);
      },
      (error)=>{
        if (error.detail){
            this.toastyService.error(error.error.detail);
        }
        for( var key in error.error){
            var x = 'error.error.'+key;
            this.toastyService.error(key.toUpperCase()+": "+eval(x)[0]);
        }
      })
    }
    if (this.multiSelect){
      let list_delete = this.multiSelectedList.map((s)=>s.id);
      this.http.StudentDeleteList(list_delete).subscribe((data)=>{
        this.getStudents((this.currentPage-1)*this.numberPerPage);
      },
      (error)=>{
        if (error.detail){
            this.toastyService.error(error.error.detail);
        }
        for( var key in error.error){
            var x = 'error.error.'+key;
            this.toastyService.error(key.toUpperCase()+": "+eval(x)[0]);
        }
      })
    }
  }

  onClickUpdate = () => {
    this.http.StudentUpdate(this.selected).subscribe((data)=>{
      this.getStudents((this.currentPage-1)*this.numberPerPage);
      $('#btnCloseUpdateModal').click();
    },
    (error)=>{
      if (error.detail){
          this.toastyService.error(error.error.detail);
      }
      for( var key in error.error){
          var x = 'error.error.'+key;
          this.toastyService.error(key.toUpperCase()+": "+eval(x)[0]);
      }
    })
  }

  onClickSave = ()=>{
    this.http.StudentCreate(this.new_student).subscribe((data:any)=>{
      this.getStudents((this.currentPage-1)*this.numberPerPage);
      $('#btnCloseAddModal').click();
      this.new_student = new Stutdent;
    },
    (error)=>{
      if (error.detail){
          this.toastyService.error(error.error.detail);
      }
      for( var key in error.error){
          var x = 'error.error.'+key;
          this.toastyService.error(key.toUpperCase()+": "+eval(x)[0]);
      }
    })
  }

  onClickSearch = () =>{
    this.onSearching=true;
    this.getStudents(0,this.search);
  }
  
  turnOffSearch = () =>{
    this.onSearching=false;
    this.getStudents(0);
  }

  onChangeHasSibling = (obj:any,value:boolean)=>{
    obj.has_other_siblings_study=value;
  }
}
