import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';
import { Plan } from '../crops/plan/plan';

@Injectable({
  providedIn: 'root'
})
export class PlanService {

  public postUrl = 'http://localhost:5000/plan';

  httpOptions = {
    headers: new HttpHeaders({
      'Authorization': 'Bearer ',
      'Content-Type': 'application/json'
    })
  };

  constructor(private http: HttpClient) {
  }

  postPlan(plan: Plan):  Observable<String> {
    return this.http.post<String>(this.postUrl, plan, this.httpOptions);
  }

}
