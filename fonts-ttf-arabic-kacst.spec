%define name fonts-ttf-arabic-kacst
%define name_orig kacst_fonts
%define srcname KacstArabicFonts-2.0
%define version 2.0
%define release %mkrel 8
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
BuildRequires: fontconfig
BuildRoot:	%_tmppath/%name-%version-%release-buildroot
BuildRequires:	mkfontscale
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
mkfontscale
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


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 2.0-6mdv2011.0
+ Revision: 675408
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 2.0-5
+ Revision: 675172
- rebuild for new rpm-setup

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0-4
+ Revision: 664321
- mass rebuild

* Fri Dec 03 2010 Funda Wang <fwang@mandriva.org> 2.0-3mdv2011.0
+ Revision: 605823
- fix build

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 2.0-2mdv2010.1
+ Revision: 494119
- fc-cache is now called by an rpm filetrigger

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - Update to 2.0 (2.01 gives some errors about font scaling and 2.0
      is the version in Fedora too)
    - Change url to Arabeyes as it's maintained by them now

* Tue Oct 06 2009 Thierry Vignaud <tv@mandriva.org> 1.6.3-9mdv2010.0
+ Revision: 454755
- do not package huge (1.2Mb) license.txt, it's GPLv2 with
  ArabeyesFonts-1.1.tar.bz2 appended...

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.6.3-8mdv2009.1
+ Revision: 351039
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.6.3-7mdv2009.0
+ Revision: 220857
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.6.3-6mdv2008.1
+ Revision: 170834
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.6.3-5mdv2008.1
+ Revision: 149734
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- buildrequires obsoletes buildprereq

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 05 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.6.3-4mdv2008.0
+ Revision: 48737
- fontpath.d conversion (#31756)
- minor cleanups


* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 23:10:22 (52883)
- Normalize fonts with new paths

* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 21:08:34 (52811)
- import fonts-ttf-arabic-kacst-1.6.3-2mdk

* Tue Feb 07 2006 Frederic Crozat <fcrozat@mandriva.com> 1.6.3-2mdk
- Don't package fonts.cache-2 file
- Fix prereq
- touch parent directory to workaround rpm changing directory last modification
  time (breaking fontconfig cache consistency detection)
- Remove dependency on freetype, this is old stuff

* Thu Aug 05 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.6.3-1mdk
- rpmlint fix
- do not use subsheels b/c they hide errors
- initial build (Munzir Taha <munzirtaha@newhorizons.com.sa>)

