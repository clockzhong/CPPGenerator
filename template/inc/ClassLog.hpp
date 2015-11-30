#ifndef CLASSLOG_HPP
#define CLASSLOG_HPP
#include <iostream>
using namespace std;
#ifndef ELPP_DISABLE_INFO_LOGS
#include <easylogging++.h>
#define I(output) LOG(INFO) << output << " in " << __FUNCTION__ <<"(), file:" << __FILE__ << ", line:" << __LINE__
#define E(output) LOG(ERROR) << output << " in " << __FUNCTION__ <<"(), file:" << __FILE__ << ", line:" << __LINE__
#else
#define I(output) 
#define E(output) cout << output << endl
#define INITIALIZE_EASYLOGGINGPP
#endif //ELPP_DISABLE_INFO_LOGS
#endif //CLASSLOG_HPP
