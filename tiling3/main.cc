#include "BallTiling.h"

int main(int argc, char *argv[])
{
   BallTiling balltiling;
   balltiling.process_command_line(argc, argv);
   balltiling.init();

   double maxr = 2.01;
   double minR = 0;
   const vector<vec3d> &verts = geom.verts();
   const vector<vector<int> > &faces = geom.faces();
   double tmp;
   double Rmin(2.01);
   double Rmax(0);
   double a;
   vec3d center,newcenter;
   vec3d e1,e2;
   double newr(2.01);
   TFile output("output.root","RECREATE");
   TNtuple nt("nt","nt","r");
   for(unsigned int i=0; i<faces.size(); ++i) {
     if(faces[i].size()==6)
     {
       for(unsigned int j=0; j<3; ++j) {
	 tmp = (verts[faces[i][j]] - verts[faces[i][j+2]]).mag();
	 maxr = maxr<tmp ? maxr : tmp;
	 minR = minR>tmp ? minR : tmp;
	 a = verts[faces[i][j]].mag();
	 Rmin = Rmin<a?Rmin:a;
	 Rmax = Rmax>a?Rmin:a;
	 a = verts[faces[i][j+3]].mag();
	 Rmin = Rmin<a?Rmin:a;
	 Rmax = Rmax>a?Rmin:a;
       }
     }
     else
     {
       cout<<"Face: "<<faces[i].size()<<endl;
       for(unsigned int j=0; j<faces[i].size()-1; ++j) 
       {
	 cout<<(verts[faces[i][j]]-verts[faces[i][j+1]]).mag()<<" ";
	 a = verts[faces[i][j]].mag();
	 Rmin = Rmin<a?Rmin:a;
	 Rmax = Rmax>a?Rmin:a;
       }
       cout<<endl;
       for(unsigned int j=0; j<faces[i].size()-1; ++j) 
	 for(unsigned int k=j; k<faces[i].size(); ++k)
	   cout<<(verts[faces[i][j]]-verts[faces[i][k]]).mag()<<" ";
       cout<<endl;
     }

     center = vec3d::zero;
     for(unsigned int j=0; j<faces[i].size(); ++j) 
     {
       center +=verts[faces[i][j]];
     }
     center /= faces[i].size();
     rand_gen randgen;
     double bestr(0.);
     double bestrr(2.01);
     double mag(0.07);
     double distance;
     const int MAXTRY(40);
     e1=(verts[faces[i][1]]-verts[faces[i][0]])*mag/MAXTRY;
     e2=(verts[faces[i][2]]-verts[faces[i][1]])*mag/MAXTRY;
     int size = faces[i].size();
     for(int j = -MAXTRY+1;j<MAXTRY;++j)
     for(int k = -MAXTRY+1;k<MAXTRY;++k)
     {
       if(fabs(j+k)>MAXTRY) continue;
       //newcenter = center+mag*vec3d::random(randgen);
       newcenter = center+e1*j+e2*k;
       //vec3d::random(randgen).dump();
       //newcenter.dump();
       for(unsigned int k=0; k<size; ++k)
       {
	 distance = theDistance(newcenter,verts[faces[i][k]],verts[faces[i][(k+1)%size]]);
	 //cout<<distance<<endl;
	 //bestrr < all distance
	 bestrr = bestrr<distance?bestrr:distance;
       }
       bestr = bestr>bestrr?bestr:bestrr; //the bigger, the better
     }
     nt.Fill(bestr);
     newr = newr<bestr?newr:bestr; //newr < all bestr
   }
   nt.Write();
   output.Close();
   cout<<"Max R:"<<Rmax<<endl;
   cout<<"Min R:"<<Rmin<<endl;
   cout<<"Max r:"<<maxr/2.<<endl;
   cout<<"Max r:"<<minR/2.<<endl;
   cout<<"Best r:"<<newr<<endl;

   return 0;
}
