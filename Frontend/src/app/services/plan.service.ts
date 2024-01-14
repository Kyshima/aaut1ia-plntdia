import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';
import { AG } from '../crops/plan/AG';
import { ACO } from '../crops/plan/ACO';

@Injectable({
  providedIn: 'root'
})
export class PlanService {

  public postUrlACO = 'http://localhost:5001/planning/antColony';
  public postUrlAG = 'http://localhost:5001/planning/geneticAlgorithm';

  httpOptions = {
    headers: new HttpHeaders({
      'Authorization': 'Bearer ',
      'Content-Type': 'application/json'
    })
  };

  constructor(private http: HttpClient) {
  }

  postACO(aco: ACO):  Observable<String> {
    return this.http.post<String>(this.postUrlACO, aco, this.httpOptions);
  }

  postAG(ag: AG):  Observable<String> {
    return this.http.post<String>(this.postUrlAG, ag, this.httpOptions);
  }

}
