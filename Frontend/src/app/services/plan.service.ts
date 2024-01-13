import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';
import {Food} from '../packages/food/food';

@Injectable({
  providedIn: 'root'
})
export class PlanService {

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

//   postFoodJava(food: Food): Observable<String> {
//     return this.http.post<String>(this.javaUrl, food, this.httpOptions);
//   }

//   postFoodProlog(food: Food): Observable<String> {

//     const fragile = food.fragile ? "yes" : "no";
//     const liquid = food.liquid ? "yes" : "no";
//     const big = food.big ? "big" : "small";

//     let url = this.prologUrl + food.category + '?fragile=' + fragile + '&liquid=' + liquid + '&size=' + big + '&units=' + food.units;
//     return this.http.get<String>(url, this.httpOptions);
//   }

}
