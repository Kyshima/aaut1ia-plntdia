export class Health {

  constructor(
    public category: string,
    public medicine: boolean,
    public first_aid: boolean,
    public hygiene: boolean,
    public liquid: boolean,
    public temp_friendly: boolean,
    public fragile: boolean,
    public units: number,
    public length?: number,
    public width?: number,
    public height?: number,
    public budget?: number
  ) {
  }


}
