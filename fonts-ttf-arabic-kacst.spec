%define oname kacst_fonts
%define srcname KacstArabicFonts-2.0
%define fontdir	fonts/TTF/arabic/kacst

Summary:	Arabic TrueType fonts
Name:		fonts-ttf-arabic-kacst
Version:	2.0
Release:	11
License:	GPLv2
Group:		System/Fonts/True type
Url:		http://www.arabeyes.org/resources.php
Source0:	http://downloads.sourceforge.net/project/arabeyes/kacst_fonts/%{oname}_%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	mkfontscale
Requires:	common-licenses
Provides:	fonts-ttf-arabic

%description
This Package provides Free Arabic TrueType fonts donated under the GPL license
by King Abdul-Aziz City for Science and Technology (KACST).

Now maintained by Arabeyes http://www.arabeyes.org

%prep
%setup -qn %{srcname}

%build

%install
mkdir -p %{buildroot}/%{_datadir}/%fontdir
cp *.ttf %{buildroot}/%{_datadir}/%fontdir

pushd %{buildroot}/%{_datadir}/%fontdir
mkfontscale
cp fonts.scale fonts.dir
popd

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/%fontdir \
	%{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-arabic-kacst:pri=50

%files
%dir %{_datadir}/%fontdir
%{_datadir}/%fontdir/*
%{_sysconfdir}/X11/fontpath.d/ttf-arabic-kacst:pri=50

