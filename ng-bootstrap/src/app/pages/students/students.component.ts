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
  preBtn:any;
  nextBtn:any;
  currentPage:any = 1;
  pages:any;
  numberPerPage:number = 10;
  new_student:Stutdent = new Stutdent;
  multiSelect:any = false;
  multiSelectedList = [];
  selectClass = [{"class_id":1,"class_cd":"TCV_DH1"},
                {"class_id":2,"class_cd":"TCV_DH2"}]
  selectClassGroup = [{"class_group_id":1,"class_group_cd":"Dài hạn tại trường"},
                {"class_group_id":2,"class_group_cd":"Dài hạn tại trung tâm"}]

  constructor(private http:HttpService,
            private toastyService:ToastyService) {
  	this.getStudents((this.currentPage-1)*this.numberPerPage);
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

  getStudents = (page?) => {
    this.http.StudentList(page).subscribe((data:any)=>{
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

}
