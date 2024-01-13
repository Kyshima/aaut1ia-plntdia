export class Predict {

  constructor(
    public state: string,
    public crop: string,
    public area: number,
    public prodAnt1: number,
    public areaAnt1: number,
    public prodAnt2?: number,
    public areaAnt2?: number,
    public prodAnt3?: number,
    public areaAnt3?: number
  ) {
  }


}
