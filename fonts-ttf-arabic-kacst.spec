%define name fonts-ttf-arabic-kacst
%define name_orig kacst_fonts
%define srcname KacstArabicFonts-2.0
%define version 2.0
%define release %mkrel 2
%define fontdir	fonts/TTF/arabic/kacst

Name:		%{name}
Summary:	Arabic TrueType fonts
Version:	%{version}
Release:	%{release}
License:	GPLv2
Group:		System/Fonts/True type
Source:		http://downloads.sourceforge.net/project/arabeyes/kacst_fonts/%{name_orig}_%{version}.tar.bz2
URL:		http://www.arabeyes.org/resources.php
BuildArch:	noarch
BuildRoot:	%_tmppath/%name-%version-%release-buildroot
BuildRequires:	freetype-tools
Requires:	common-licenses
Provides:	fonts-ttf-arabic

%description
This Package provides Free Arabic TrueType fonts donated under the GPL license
by King Abdul-Aziz City for Science and Technology (KACST).

Now maintained by Arabeyes http://www.arabeyes.org

%prep
%setup -q -n %{srcname}

%build

%install
rm -rf %buildroot

mkdir -p %buildroot/%_datadir/%fontdir
cp *.ttf %buildroot/%_datadir/%fontdir

pushd %buildroot/%_datadir/%fontdir
%_sbindir/ttmkfdir -u -o fonts.scale
cp fonts.scale fonts.dir
popd

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/%fontdir \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-arabic-kacst:pri=50

%clean
rm -rf %buildroot

%files
%defattr(0644,root,root,0755)
%dir %_datadir/%fontdir
%_datadir/%fontdir/*
%_sysconfdir/X11/fontpath.d/ttf-arabic-kacst:pri=50
