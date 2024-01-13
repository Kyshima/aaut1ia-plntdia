import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CropsComponent } from './crops.component';

describe('FoodComponent', () => {
  let component: CropsComponent;
  let fixture: ComponentFixture<CropsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CropsComponent]
    });
    fixture = TestBed.createComponent(CropsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
