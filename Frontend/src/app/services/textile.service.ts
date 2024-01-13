import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';
import {Textile} from '../packages/textile/textile';

@Injectable({
  providedIn: 'root'
})
export class TextileService {

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

  postTextileJava(textile: Textile): Observable<String> {
    return this.http.post<String>(this.javaUrl, textile, this.httpOptions);
  }

  postTextileProlog(textile: Textile): Observable<String> {

    const delicate = textile.delicate ? "yes" : "no";
    const big = textile.big ? "big" : "small";

    let url = this.prologUrl + textile.category + '?fragile=' + delicate + '&size=' + big + '&units=' + textile.units;
    return this.http.get<String>(url, this.httpOptions);
  }

}
