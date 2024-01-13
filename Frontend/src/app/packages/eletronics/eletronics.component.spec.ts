import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EletronicsComponent } from './eletronics.component';

describe('EletronicsComponent', () => {
  let component: EletronicsComponent;
  let fixture: ComponentFixture<EletronicsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [EletronicsComponent]
    });
    fixture = TestBed.createComponent(EletronicsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
