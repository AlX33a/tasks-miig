public class FlatSegment extends Segment {

    public GeodesyPoint point_1;
    public GeodesyPoint point_2;

    public FlatSegment (GeodesyPoint point_1, GeodesyPoint point_2) {
        super(point_1, point_2);
        this.point_1 = point_1;
        this.point_2 = point_2;
    }

    public FlatSegment (FlatSegment fs) {
        super(fs.point_1, fs.point_2);
        this.point_1 = fs.point_1;
        this.point_2 = fs.point_2;
    }

    public FlatSegment turnSegment (GeodesyPoint gp, double angleMultiplier) {
        return new FlatSegment(point_1.turnPointRelatively(gp, angleMultiplier), point_2.turnPointRelatively(gp, angleMultiplier));
    }
}
