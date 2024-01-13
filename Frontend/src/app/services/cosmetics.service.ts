import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';
import {Cosmetics} from '../packages/cosmetics/cosmetics';

@Injectable({
  providedIn: 'root'
})
export class CosmeticsService {

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

  postCosmeticsJava(cosmetics: Cosmetics): Observable<String> {
    return this.http.post<String>(this.javaUrl, cosmetics, this.httpOptions);
  }

  postCosmeticsProlog(cosmetics: Cosmetics): Observable<String> {

    const fragile = cosmetics.fragile ? "yes" : "no";
    const liquid = cosmetics.liquid ? "yes" : "no";
    const big = cosmetics.big ? "big" : "small";

    let url = this.prologUrl + cosmetics.category + '?fragile=' + fragile + '&liquid=' + liquid + '&size=' + big + '&units=' + cosmetics.units;
    return this.http.get<String>(url, this.httpOptions);
  }

}
