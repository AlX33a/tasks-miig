public class Segment extends Vector {

    private Point startPoint;
    private Point endPoint;

    public Segment(Point startPoint, Point endPoint) {
        super(startPoint, endPoint);
        this.startPoint = startPoint;
        this.endPoint = endPoint;
    }

    public boolean containsPoint(Point point) {
        Segment startPointPointSegment = new Segment(this.startPoint, point);
        Segment endPointPointSegment = new Segment(this.endPoint, point);
        double startPointPointSegmentModulo = startPointPointSegment.get_modulo();
        double endPointPointSegmentModulo = endPointPointSegment.get_modulo();
        double moduloSum = startPointPointSegmentModulo + endPointPointSegmentModulo;
        if (moduloSum == this.get_modulo()) {
            return true;
        } else {
            return false;
        }

    }

    public boolean intersectsSegment(Segment segment) {
        Segment s_1 = new Segment(this.startPoint, segment.endPoint);
        Segment s_2 = new Segment(this.startPoint, segment.startPoint);

        double pseudoScalar_1 = this.pseudoscalar_product(s_1);
        double pseudoScalar_2 = this.pseudoscalar_product(s_2);

        if (pseudoScalar_1 * pseudoScalar_2 < 0) {
            return true;
        } else {
            return false;
        }
    }
}
