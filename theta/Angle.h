#ifndef Angle_H
#define Angle_H
class Angle
{
  public:
    void read(double x1,double y1,double z1,double x2,double y2,double z2,double R);
    double theta();
  private:
    double m_x1,m_y1,m_z1,m_x2,m_y2,m_z2,m_R;
};
#endif
