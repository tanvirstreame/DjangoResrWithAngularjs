import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import {HttpClient} from '@angular/common/http';
import {IStudent} from './student';
@Injectable({
  providedIn: 'root'
})
export class GetStudentService {

private url:string="http://localhost:5000/StudentInfo/";

  constructor(private http:HttpClient) {}
    getStudent():Observable<IStudent[]>{
    return this.http.get<IStudent[]>(this.url);
}}
