import java.util.ArrayList;
import java.util.Arrays;


public class BrokenLine {
    
    private ArrayList<Point> pointsList = new ArrayList<>();
    private ArrayList<Segment> segmentsList = new ArrayList<>();
    private double length;
    
    public BrokenLine (Point ...points) {
        this.pointsList = new ArrayList<Point>(Arrays.asList(points));
        
        for (int i = pointsList.size() - 1; i > 0; i--) {
            Segment segment = new Segment(pointsList.get(i), pointsList.get(i - 1));
            this.segmentsList.add(segment);
            this.length += segment.get_modulo();
        }
    }

    public BrokenLine (Segment ...segments) {
        this.segmentsList = new ArrayList<Segment>(Arrays.asList(segments));

        for (Segment segment: segmentsList) {
            this.length += segment.get_modulo();
        }
    }

    public double getLength() {
        return this.length;
    }

    public boolean containsPoint(Point point) {
        for (Segment segment: this.segmentsList) {
            if (segment.containsPoint(point)) {
                return true;
            }
        }
        return false;
    }

    public boolean intersectsSegment(Segment segment) {
        for (Segment brokenLineSegment: this.segmentsList) {
            if (brokenLineSegment.intersectsSegment(segment)) {
                return true;
            }
        }
        return false;
    }

    public boolean intersectsBrokenLine(BrokenLine anotherBrokenLine) {
        for (Segment thisBrokenLineSegment: this.segmentsList) {
            for (Segment anotherBrokenLineSegment: anotherBrokenLine.segmentsList) {
                if (thisBrokenLineSegment.intersectsSegment(anotherBrokenLineSegment)) {
                    return true;
                }
            }
        }
        return false;
    }

    public boolean isSelfIntersecting() {
        for (Segment brokenLineSegment: this.segmentsList) {
            for (Segment intersectableBrokenLineSegment: this.segmentsList) {
                if (brokenLineSegment.intersectsSegment(intersectableBrokenLineSegment)) {
                    return true;
                }
            }
        }
        return false;
    }
}
