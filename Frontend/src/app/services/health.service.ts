import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';
import {Health} from '../packages/health/health';

@Injectable({
  providedIn: 'root'
})
export class HealthService {

  public javaUrl = 'http://localhost:8080/api';
  public prologUrl = 'http://localhost:5026/';

  httpOptions = {
    headers: new HttpHeaders({
      'Authorization': 'Bearer ',
      'Content-Type': 'application/json'
    })
  };

  constructor(private http: HttpClient) {
  }

  postHealthJava(health: Health): Observable<String> {
    return this.http.post<String>(this.javaUrl, health, this.httpOptions);
  }

  postHealthProlog(health: Health): Observable<String> {

    const medicine = health.medicine ? "yes" : "no";
    const firstaid = health.first_aid ? "yes" : "no";
    const hygiene = health.hygiene ? "yes" : "no";
    const fragile = health.fragile ? "yes" : "no";
    const liquid = health.liquid ? "yes" : "no";
    const temperature = health.temp_friendly ? "yes" : "no";

    //http://localhost:5026/health?medicine=yes&firstaid=no&hygene=no&fragile=yes&liquid=no&temperature=yes&units=900
    let url = this.prologUrl + health.category + '?medicine=' + medicine + '&firstaid=' + firstaid + '&hygiene=' + hygiene + '&fragile=' + fragile + '&liquid=' + liquid + '&temperature=' + temperature + '&units=' + health.units;
    return this.http.get<String>(url, this.httpOptions);
  }

}
