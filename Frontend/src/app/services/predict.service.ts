import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';
import { Predict } from '../crops/predict/predict';

@Injectable({
  providedIn: 'root'
})
export class PredictService {

  public postUrl = 'http://localhost:8080/api';

  httpOptions = {
    headers: new HttpHeaders({
      'Authorization': 'Bearer ',
      'Content-Type': 'application/json'
    })
  };

  constructor(private http: HttpClient) {
  }

  postPredict(predict: Predict):  Observable<String> {
    return this.http.post<String>(this.postUrl, predict, this.httpOptions);
  }

}
