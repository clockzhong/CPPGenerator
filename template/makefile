include inc.cfg

SRC_PATH=./src
INC_PATH=./inc
TESTS_PATH=./tests
#We define the Env variables in this section
export GOOGLETEST_ROOT_PATH=$(SourcesRoot)/GoogleTest
export SQLITE_ROOT_PATH=$(SourcesRoot)/SQLite

CPPFLAGS += -I$(INC_PATH)

# Flags passed to the preprocessor.
# Set Google Test's header directory as a system directory, such that
# the compiler doesn't generate warnings in Google Test headers.
CPPFLAGS += -isystem $(GOOGLETEST_ROOT_PATH)/include

# Flags passed to the C++ compiler.
CPPFLAGS += -g -Wall -Wextra -pthread

# All Google Test headers.  Usually you shouldn't change this
# definition.
GTEST_HEADERS = $(GOOGLETEST_ROOT_PATH)/include/gtest/*.h \
                $(GOOGLETEST_ROOT_PATH)/include/gtest/internal/*.h

# Usually you shouldn't tweak such internal variables, indicated by a
# trailing _.
GTEST_SRCS = $(GOOGLETEST_ROOT_PATH)/src/*.cc $(GOOGLETEST_ROOT_PATH)/src/*.h $(GTEST_HEADERS)

# For simplicity and to avoid depending on Google Test's
# implementation details, the dependencies specified below are
# conservative and not optimized.  This is fine as Google Test
# compiles fast and for ordinary users its source rarely changes.
gtest-all.o : $(GTEST_SRCS)
	$(CXX) $(CPPFLAGS) -I$(GOOGLETEST_ROOT_PATH) $(CPPFLAGS) -c \
            $(GOOGLETEST_ROOT_PATH)/src/gtest-all.cc

gtest_main.o : $(GTEST_SRCS)
	$(CXX) $(CPPFLAGS) -I$(GOOGLETEST_ROOT_PATH) -c \
            $(GOOGLETEST_ROOT_PATH)/src/gtest_main.cc

gtest.a : gtest-all.o
	$(AR) $(ARFLAGS) $@ $^

gtest_main.a : gtest-all.o gtest_main.o
	$(AR) $(ARFLAGS) $@ $^

CLASS_OBJ_LIST=$(foreach myClass, $(CLASS_LIST), $(SRC_PATH)/$(myClass).o)

CLASS_TEST_OBJ_LIST=$(foreach myClass, $(CLASS_LIST), $(TESTS_PATH)/test$(myClass).o)

CLASS_TEST_LIST=$(foreach myClass, $(CLASS_LIST), $(TESTS_PATH)/test$(myClass))

OBJ_LIST=$(CLASS_OBJ_LIST) $(CLASS_TEST_OBJ_LIST)

EXTRA_APP_LIST=$(foreach EXT_APP_ITEM, $(EXT_APP_LIST), $(TESTS_PATH)/$(EXT_APP_ITEM))

libMyClass.a: $(CLASS_OBJ_LIST) gtest-all.o gtest_main.o
	$(AR) $(ARFLAGS) $@ $^


TESTS = $(CLASS_TEST_LIST) $(EXTRA_APP_LIST)

CPPFLAGS+= -std=c++11 -DVERBOSE

ifeq "$(ENABLE_LOCAL_TEST)" "1"
	CPPFLAGS+=-DENABLE_LOCAL_TEST=1
endif

CPPFLAGS+= -DSERVER_IP='"$(ServerIP)"'

CPPFLAGS+= -I$(LIBSOCKET_HEADER_PATH) -L$(LIBSOCKET_LIB_PATHS)

CPPFLAGS+=  -lsocket++

CPPFLAGS+=  -lpthread

CPPFLAGS+= -DSOCKET_PORT=8888


#Flags for SQLite path
CPPFLAGS += -I$(SQLITE_ROOT_PATH) -L$(SQLITE_ROOT_PATH)/.libs
CPPFLAGS+=  -lsqlite3

CPPFLAGS +=-I$(EASYLOGGINGPP_HEADER_PATH)

#first_test.o : first_test.cpp \
#                     $(GTEST_HEADERS)
#	$(CXX) $(CPPFLAGS) -c first_test.cpp


$(TESTS_PATH)/first_test.o: $(TESTS_PATH)/first_test.d
$(TESTS_PATH)/first_test : $(TESTS_PATH)/first_test.o gtest_main.a
	$(CXX) $(CPPFLAGS)  $^ -o $@

##define the Libsocket library paths:
export LIBSOCKET_ROOT_PATH=$(SourcesRoot)/Libsocket
#export LIBSOCKET_LIB_PATHS=$(LIBSOCKET_ROOT_PATH)/C:$(LIBSOCKET_ROOT_PATH)/C++
export LIBSOCKET_LIB_PATHS=$(LIBSOCKET_ROOT_PATH)/C++
export LIBSOCKET_HEADER_PATH=$(LIBSOCKET_ROOT_PATH)/headers

export EASYLOGGINGPP_HEADER_PATH=$(SourcesRoot)/EasyLogging++/src

srv: ./server.cpp
	$(CXX) -o $@ server.cpp $(CPPFLAGS) 

cl: ./client.cpp
	$(CXX) -o $@ client.cpp $(CPPFLAGS) 

tcpTest: srv cl


udpServer: ./udpServer.cpp
	$(CXX) -o $@ udpServer.cpp $(CPPFLAGS) 

udpClient: ./udpClient.cpp
	$(CXX) -o $@ udpClient.cpp $(CPPFLAGS) 

udpTest: udpServer udpClient


testThreadStdlib : testThreadStdlib.cpp
	$(CXX) $(CPPFLAGS)  -o $@ testThreadStdlib.cpp

testThreadStdlib2 : testThreadStdlib2.cpp
	$(CXX) $(CPPFLAGS)   -o $@ testThreadStdlib2.cpp

udpSendMeasure : udpSendMeasure.cpp
	$(CXX)  -o $@ udpSendMeasure.cpp $(CPPFLAGS) 

testPingServer.o : $(GTEST_HEADERS) testPingServer.cpp sessionClient.hpp pingServer.hpp sessionServer.hpp commandList.hpp
	$(CXX) $(CPPFLAGS)  -c testPingServer.cpp

testPingServer : testPingServer.o gtest_main.a
	$(CXX)  $^ -o $@ $(CPPFLAGS)

testPingServer2.o : $(GTEST_HEADERS) testPingServer2.cpp pingServer.hpp sessionServer.hpp commandList.hpp
	$(CXX) $(CPPFLAGS)  -c testPingServer2.cpp

testPingServer2 : testPingServer2.o gtest_main.a
	$(CXX)  $^ -o $@ $(CPPFLAGS)


#define GenerateTestFunc
#test$(1): test$(1).o libMyClass.a
#	echo AAAAAAAAAA
#endef

##$(eval $(call GenerateTestFunc, CommandItem))


####Add class test case here!

##$(TESTS_PATH)/testMyUtils : $(TESTS_PATH)/testMyUtils.o libMyClass.a
##	$(CXX)  $^ -o $@ $(CPPFLAGS)


####The above class test cases finished here

CPPFILES := $(wildcard *.cpp)

test2:
#	#echo $(CPPFILES)
	echo $(CLASS_OBJ_LIST)

# pull in dependency info for *existing* .o files
-include $(OBJ_LIST:.o=.d)

#Generate Depend files in $(SRC_PATH)
$(SRC_PATH)/%.d : $(SRC_PATH)/%.cpp
	@gcc -MM $(CPPFLAGS) $(SRC_PATH)/$*.cpp > $(SRC_PATH)/$*.d

#Compile all *.cpp files in $(SRC_PATH)
$(SRC_PATH)/%.o : $(SRC_PATH)/%.cpp $(SRC_PATH)/%.d
	gcc -c $(CPPFLAGS) -DDEBUG_$*=$(DEBUG_$*) $(SRC_PATH)/$*.cpp -o $(SRC_PATH)/$*.o


#Generate Depend files in $(TESTS_PATH)
$(TESTS_PATH)/%.d : $(TESTS_PATH)/%.cpp
	@gcc -MM $(CPPFLAGS) $(TESTS_PATH)/$*.cpp > $(TESTS_PATH)/$*.d

#Compile all *.cpp files in $(TESTS_PATH)
$(TESTS_PATH)/%.o : $(TESTS_PATH)/%.cpp $(TESTS_PATH)/%.d
	gcc -c $(CPPFLAGS) -DDEBUG_$*=$(DEBUG_$*) $(TESTS_PATH)/$*.cpp -o $(TESTS_PATH)/$*.o




all: $(TESTS)

clean:
	rm -f $(TESTS_PATH)/*.d
	rm -f $(TESTS_PATH)/*.o
	rm -f $(SRC_PATH)/*.d 
	rm -f $(SRC_PATH)/*.o 
	rm -f ./*.o
	rm -f ./*.a
	rm -f $(TESTS)

print-%:
	@echo $* is defined as: '$($*)'

