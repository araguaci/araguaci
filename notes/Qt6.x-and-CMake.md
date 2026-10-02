
# Configuring Qt 6.x and CMake for windows 10

If you want to create a redistributable installer for a Qt app with Cmake then youve come to the right place...
I ve been struggling to make Qt work with cmake on windows, and finally figure out something that works:

1. Go ahead and download Qt: https://www.qt.io/download-qt-installer

2. Start the install and select "Custom installation"
![image11](https://user-images.githubusercontent.com/885349/217992198-8587b938-438a-4fba-b6b0-8fc6ec2a407f.png)

3. Select a version of Qt with MingGW 64 (and any other lib you need like openssl for example...)
![image3](https://user-images.githubusercontent.com/885349/217992374-8b137718-4583-46d8-bd69-e93e802c326c.png)

4. Also download the installer framework:
![image4](https://user-images.githubusercontent.com/885349/217992570-2a8536c9-13b0-4995-81f2-6f6038f0f8bb.png)

5. Setup windows environment vars (note that the order matters...) for the power shell to find the tools and libs that you need.

![image6](https://user-images.githubusercontent.com/885349/217992632-485c96f9-5caa-4475-bf85-33698c600212.png)

6. Ensure you have powershell installed or get the latest version here: https://github.com/PowerShell/PowerShell

7. You need `vcredist_x64_2010.exe` to be included with your package so get it here: https://www.microsoft.com/en-us/download/details.aspx?id=26999

8. Now that everyting is installed you can create the `CMakeLists.txt` code to generate an installer:
```cmake
# Add your classic CMake stuffs...
cmake_minimum_required(VERSION 3.20)

if(${CMAKE_VERSION} VERSION_GREATER_EQUAL "3.20")
	cmake_policy(SET CMP0115 NEW)
endif()

project(
	"My Cool Project"
	VERSION 1.0.1
	DESCRIPTION "Some really awesome project that one day will change the world..."
	LANGUAGES C CXX
)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

message(STATUS "${PROJECT_NAME} ${PROJECT_VERSION} for ${CMAKE_SYSTEM_NAME} ${CMAKE_SYSTEM_PROCESSOR}")
string(TIMESTAMP PROJECT_BUILD_DATE "%Y-%m-%d")
string(TIMESTAMP PROJECT_BUILD_YEAR "%Y")
configure_file(src/build.h)

# add warnings
add_compile_options(
	-Wall
	-Wpedantic
	-Wextra
	-Wshadow
	-Wformat=2
	-Wstrict-overflow
	-fvisibility=hidden
	-fno-strict-aliasing
	-Werror
)

if(DEBUG)
	message(STATUS "DEBUG MODE: DO NOT RELEASE ANYTHING FROM THIS BUILD!")
	add_compile_options(
		-g
		-O0
	)
else()
	message(STATUS "RELEASE MODE")
	add_compile_options(
		-s
		-Os
		-DNDEBUG
	)
	set(CMAKE_POSITION_INDEPENDENT_CODE ON)
endif()

set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -s")

set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)

# Now for the Qt specific stuffs...

# Tells CMake where to find Qt, it need to be set right!
set(QT_PATH "C:/QT")
message(STATUS "QT Path: ${QT_PATH}")
set(QT_ENV_PATH "C:/QT/6.2.4/mingw_64")
message(STATUS "QT Env: ${QT_ENV_PATH}")

# MS Redistributable path
set(MS_VCR100 "C:/Windows/System32")

# If you are using some libraries provided by Qt, here with OpenSSL:
target_include_directories(encryption PUBLIC "${QT_PATH}/Tools/OpenSSL/Win_x64/include")
target_link_directories(encryption PUBLIC "${QT_PATH}/Tools/OpenSSL/Win_x64/lib" "${QT_PATH}/Tools/OpenSSL/Win_x64/bin")


set(CMAKE_AUTOMOC ON)
find_package(Qt6 REQUIRED COMPONENTS Core Widgets)


# Add you beautifull executable
add_executable(
	my_exe
	WIN32
	src/build.h
	src/main.cxx
	src/something.cxx
	src/something.hxx
)

set_target_properties(my_exe PROPERTIES
	WIN32_EXECUTABLE TRUE
)
target_link_libraries(
	my_exe
	PUBLIC
	Qt6::Widgets
	Qt6::Core
	encryption
)

install(
	TARGETS my_exe
	RUNTIME DESTINATION .
	COMPONENT my_exe_installer
	BUNDLE DESTINATION .
	COMPONENT my_exe_installer
)

function(CPACKIFW_COMMON)
	set(CPACK_PACKAGE_NAME my_exe)
	set(CPACK_PACKAGE_FILE_NAME "setup_${CPACK_PACKAGE_NAME}V${PROJECT_VERSION}")
	set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "A beautifull program")
	set(CPACK_PACKAGE_VERSION "${PROJECT_VERSION}")
	set(CPACK_PACKAGE_INSTALL_DIRECTORY "${CPACK_PACKAGE_NAME}")
	set(CPACK_COMPONENTS_ALL my_exe_installer)
	set(CPACK_IFW_PACKAGE_START_MENU_DIRECTORY "My Exe")
	set(CPACK_IFW_PACKAGE_PUBLISHER "Fred")
	set(CPACK_GENERATOR IFW)
	set(CPACK_IFW_VERBOSE ON)
	set(CPACK_IFW_PACKAGE_WIZARD_STYLE Classic)
	set(CPACK_CREATE_DESKTOP_LINKS "My Exe")

	include(CPack REQUIRED)
	include(CPackIFW REQUIRED)

	cpack_add_component(
		my_exe_installer
		DISPLAY_NAME "My Exe"
		DESCRIPTION "My Exe description"
		REQUIRED
	)

	cpack_ifw_configure_component(
		my_exe_installer
		FORCED_INSTALLATION
		NAME qt.my_exe.installer
		VERSION ${PROJECT_VERSION} # Version of component
		DEFAULT TRUE
	)
endfunction()

add_custom_command(
	TARGET my_exe POST_BUILD
	COMMAND ${CMAKE_COMMAND} -E remove_directory ${CMAKE_BINARY_DIR}/windeployqt_stuff
	COMMAND windeployqt.exe --compiler-runtime --dir ${CMAKE_BINARY_DIR}/windeployqt_stuff $<TARGET_FILE:my_exe>
)

# some required Qt components
install(
	DIRECTORY ${CMAKE_BINARY_DIR}/windeployqt_stuff/
	DESTINATION .
	COMPONENT my_exe_installer
)

# optionally add some custom DLLs
install(
	DIRECTORY "src/dll/"
	DESTINATION .
	COMPONENT my_exe_installer
	FILES_MATCHING PATTERN "*"
)

# optionally adds some files, here a default config file that goes in the config directory
install(
	FILES "src/pkg/config.ini"
	DESTINATION config
	COMPONENT my_exe_installer
)

# optionally add some of Qt DLLs
install(
	DIRECTORY "${QT_PATH}/Tools/OpenSSL/Win_x64/bin/"
	DESTINATION .
	COMPONENT my_exe_installer
	FILES_MATCHING PATTERN "*.dll"
)

# required platforms plugins
install(
	DIRECTORY "${QT_ENV_PATH}/plugins/platforms/"
	DESTINATION .
	COMPONENT my_exe_installer
	FILES_MATCHING PATTERN "*.dll"
)

# required redistributables
install(
	FILES
	"${MS_VCR100}/msvcr100.dll"
	"${MS_VCR100}/msvcr100_clr0400.dll"
	"${MS_VCR100}/msvcrt.dll"
	DESTINATION .
	COMPONENT my_exe_installer
)

CPACKIFW_COMMON()

```

9. Now that you have a working CMake file you can go ahead and build your project:
```sh
# always use a new dir for the build
mkdir build
cd build

# gen the cmake environment
cmake ../ -G "MinGW Makefiles"

# compile
mingw32-make.exe -j 4

# generate the installer package
mingw32-make.exe package
```

Enjoy your new installer package!
