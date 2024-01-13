import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';
import {Eletronics} from '../packages/eletronics/eletronics';

@Injectable({
  providedIn: 'root'
})
export class EletronicsService {

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

  postEletronicsJava(eletronics: Eletronics): Observable<String> {
    return this.http.post<String>(this.javaUrl, eletronics, this.httpOptions);
  }

  postEletronicsProlog(eletronics: Eletronics): Observable<String> {


    const heavy = eletronics.heavy ? "heavy" : "light";
    const big = eletronics.big ? "big" : "small";
    const fragile = eletronics.fragile ? "yes" : "no";
    const visibility = eletronics.visibility ? "yes" : "no";
    const resistant = eletronics.resistant ? "yes" : "no";


    //http://localhost:5026/eletronics?size=small&fragile=yes&resist=yes&visibility=yes&units=1100&weight=heavy
    let url = this.prologUrl + eletronics.category + '?size=' + big + '&fragile=' + fragile + '&resist=' + resistant + '&visibility=' + visibility + '&units=' + eletronics.units + '&weight=' + heavy;
    return this.http.get<String>(url, this.httpOptions);
  }

}
