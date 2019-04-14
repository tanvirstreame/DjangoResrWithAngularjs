import { Component, OnInit } from '@angular/core';
import {GetStudentService } from './getstudent.service' ;
@Component({
  selector: 'app-student-detail',
  templateUrl: './student-detail.component.html',
  styleUrls: ['./student-detail.component.css']
})
export class StudentDetailComponent implements OnInit {
public student=[];
  constructor(private _student:GetStudentService) { }

  ngOnInit() {
   this._student.getStudent().subscribe((res : any[])=>{
        console.log(res);
        this.student=res;});
  }

}
