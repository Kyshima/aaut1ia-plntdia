import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';
import {Packages} from '../packages/packages';
import { Router } from '@angular/router';


@Injectable({
  providedIn: 'root'
})
export class PackagesService {

  
  constructor(private router: Router) { }

  navigateToHealth() {
    this.router.navigate(['/health']); // Replace 'other' with the path of the page you want to navigate to
  }

  navigateToFood() {
    this.router.navigate(['/food']); // Replace 'other' with the path of the page you want to navigate to
  }

  navigateToCosmetics() {
    this.router.navigate(['/cosmetics']); // Replace 'other' with the path of the page you want to navigate to
  }

  navigateToEletronics() {
    this.router.navigate(['/eletronics']); // Replace 'other' with the path of the page you want to navigate to
  }

  navigateToFurniture() {
    this.router.navigate(['/furniture']); // Replace 'other' with the path of the page you want to navigate to
  }

  navigateToTextile() {
    this.router.navigate(['/textil']); // Replace 'other' with the path of the page you want to navigate to
  }

  

  

}
