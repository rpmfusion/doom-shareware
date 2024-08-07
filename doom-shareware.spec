Name:           doom-shareware
Version:        1.9
Release:        26.s%{?dist}
Summary:        Official shareware game files for DOOM
Group:          Amusements/Games
License:        Distributable
URL:            https://www.idsoftware.com
Source0:        ftp://ftp.idsoftware.com/idstuff/doom/doom19s.zip
Source1:        doom-shareware.metainfo.xml
Source2:        doom-shareware-wad-license.txt
BuildRequires:  libappstream-glib
BuildArch:      noarch
# Uncomment this once rpm on the buildsys is new enough
#Supplements:    chocolate-doom prboom vavoom
#Suggests:       vavoom-doom-shareware

%description
The official iwad file for the shareware version of Doom. This can be
played with a doom engine of your choice, i.e. chocolate-doom, prboom
or vavoom.


%prep
%setup -q -c -n doom19s
cat DOOMS_19.1 DOOMS_19.2 > DOOMS_19.zip
unzip -qq DOOMS_19.zip
cp %{SOURCE2} .
sed -i 's/\r//' README.TXT


%build
# Game data files.  Nothing to build!


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/games/doom
install -pD -m 0644 DOOM1.WAD $RPM_BUILD_ROOT%{_datadir}/games/doom/doom1.wad
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.metainfo.xml


%files
%doc README.TXT
%license doom-shareware-wad-license.txt
%{_datadir}/games/doom
%{_datadir}/appdata/%{name}.metainfo.xml


%changelog
* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.9-26.s
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.9-25.s
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.9-24.s
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.9-23.s
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.9-22.s
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.9-21.s
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.9-20.s
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.9-19.s
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.9-18.s
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.9-17.s
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.9-16.s
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.9-15.s
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 1.9-14.s
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.9-13.s
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.9-12.s
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.9-11.s
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan  4 2016 Hans de Goede <j.w.r.degoede@gmail.com> - 1.9-10.s
- Stop providing a launcher / icon this results in doom showing twice in
  the app menu when users also have vavoom from Fedora installed which
  is quite ugly / confusing. The launcher shipped with vavoom >= 1.33-15
  will use the wad file from this pkg if present (rf#411)
- Simply start "prboom" to get the old launcher behavior
- Move the wad file from /usr/share/doom-shareware/DOOM1.WAD to
  /usr/share/games/doom/doom1.wad where most implementations will
  automatically find it
- Add an appstream metainfo file making this an addon to chocolate-doom,
  prboom and vavoom

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.9-9.s
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.9-8.s
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.9-7.s
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.9-6.s
- rebuild for new F11 features

* Thu Jul 24 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.9-5.s
- Release bump for rpmfusion build

* Tue Mar 27 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.9-4.s
- Fix unowned /usr/share/doom-shareware directory

* Sun Sep 24 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.9-3.s
- Rebuild for FC-6

* Fri Aug 18 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.9-2.s
- Add doom-logo.png to svn

* Tue Aug  1 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.9-1.s
- Change version from 19s to 1.9 add 's' part of version to release
- Make vendor and category livna instead of fedora
- Add missing BR desktop-file-utils
- Various specfile cleanups

* Mon Mar  6 2006 Wart <wart at kobold.org> 19s-1
- Initial package for Fedora Extras
