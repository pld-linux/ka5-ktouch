%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		ktouch
Summary:	ktouch
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	3d8b1ebbe806f76c916ef1bd67d0c2d4
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Script-devel
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5X11Extras-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	Qt5XmlPatterns-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.30.0
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kcompletion-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kitemviews-devel
BuildRequires:	kf5-ktextwidgets-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-qtdeclarative >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KTouch is a program to learn and practice touch typing. Every finger
has its place on the keyboard with associated keys to press. Starting
with only a few keys to remember you will advance through different
training levels where additional keys are introduced.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktouch
%{_desktopdir}/org.kde.ktouch.desktop
%{_datadir}/config.kcfg/ktouch.kcfg
%{_iconsdir}/hicolor/128x128/apps/ktouch.png
%{_iconsdir}/hicolor/16x16/apps/ktouch.png
%{_iconsdir}/hicolor/22x22/apps/ktouch.png
%{_iconsdir}/hicolor/32x32/apps/ktouch.png
%{_iconsdir}/hicolor/48x48/apps/ktouch.png
%{_iconsdir}/hicolor/scalable/apps/ktouch.svgz
%{_datadir}/ktouch
%{_mandir}/ca/man1/ktouch.1*
%{_mandir}/de/man1/ktouch.1*
%{_mandir}/es/man1/ktouch.1*
%{_mandir}/et/man1/ktouch.1*
%{_mandir}/fr/man1/ktouch.1*
%{_mandir}/gl/man1/ktouch.1*
%{_mandir}/it/man1/ktouch.1*
%{_mandir}/man1/ktouch.1*
%{_mandir}/nl/man1/ktouch.1*
%{_mandir}/pl/man1/ktouch.1*
%{_mandir}/pt/man1/ktouch.1*
%{_mandir}/pt_BR/man1/ktouch.1*
%{_mandir}/sv/man1/ktouch.1*
%{_mandir}/uk/man1/ktouch.1*
%{_datadir}/metainfo/org.kde.ktouch.appdata.xml
