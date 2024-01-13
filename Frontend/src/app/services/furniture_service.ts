import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';
import {Health} from '../packages/health/health';
import {Furniture} from "../packages/furniture/furniture";

@Injectable({
  providedIn: 'root'
})
export class FurnitureService {

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

  postFurnitureJava(furniture: Furniture): Observable<String> {
    return this.http.post<String>(this.javaUrl, furniture, this.httpOptions);
  }

  postFurnitureProlog(furniture: Furniture): Observable<String> {

    const size = furniture.big ? "big" : "small";
    const soldIn = furniture.pieces ? "pieces" : "whole";
    const fragile = furniture.fragile ? "yes" : "no";

    let url = this.prologUrl + furniture.category + '?size=' + size + '&soldIn=' + soldIn + '&fragile=' + fragile + '&units=' + furniture.units;
    return this.http.get<String>(url, this.httpOptions);
  }

}
