#include "antiprism/antiprism.h" //for vec3d etc
#include "Tiling.h"

class BallTiling: public prog_opts {
   public:
      string ifile;
      string ofile;

      void process_command_line(int argc, char **argv);
      void usage();
      void init();
   private:
      col_geom_v m_geom;
};


void BallTiling::usage()
{
   fprintf(stdout,
"\n"
"To be implemented"
"\n", prog_name(), help_ver_text);
}

void BallTiling::process_command_line(int argc, char **argv)
{
   opterr = 0;
   
   handle_long_opts(argc, argv);

   if(argc-optind > 1)
      error("too many arguments");
   
   if(argc-optind == 1)
      ifile=argv[optind];
}

void BallTiling::init()
{
   char errmsg[MSG_SZ];
   if(!m_geom.read(balltiling.ifile, errmsg))
      balltiling.error(errmsg);
   if(*errmsg)
      balltiling.warning(errmsg);
}
