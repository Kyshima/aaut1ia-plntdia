import {Component} from '@angular/core';
import {Packages} from "./packages";
import {PackagesService} from "../services/packages.service";

@Component({
  selector: 'app-health',
  templateUrl: './packages.component.html',
  styleUrls: ['./packages.component.css']
})
export class PackagesComponent {

  constructor(private packagesService: PackagesService) {
  }

  navigateToFood() {
    this.packagesService.navigateToFood();
  }

  navigateToHealth() {
    this.packagesService.navigateToHealth(); 
  }

  navigateToCosmetics() {
    this.packagesService.navigateToCosmetics();
  }

  navigateToEletronics() {
    this.packagesService.navigateToEletronics(); 
  }

  navigateToFurniture() {
    this.packagesService.navigateToFurniture();
  }

  navigateToTextile() {
    this.packagesService.navigateToTextile();
  }

  



}
