Name:           doom-shareware
Version:        1.9
Release:        7.s%{?dist}
Summary:        Official shareware game files for DOOM
Group:          Amusements/Games
License:        Distributable
URL:            http://www.idsoftware.com
Source0:        ftp://ftp.idsoftware.com/idstuff/doom/doom19s.zip
Source1:        doom19s.desktop
Source2:        doom-shareware-wad-license.txt
Source3:        doom-logo.png
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  desktop-file-utils
BuildArch:      noarch
Requires:       prboom hicolor-icon-theme

%description
The official iwad file for the shareware version of Doom.


%prep
%setup -q -c -n doom19s
cat DOOMS_19.1 DOOMS_19.2 > DOOMS_19.zip
unzip -qq DOOMS_19.zip
cp %{SOURCE2} .
sed -i 's/\r//' README.TXT


%build
# Game data files.  Nothing to build!


%install
rm -rf $RPM_BUILD_ROOT
install -pD -m 0644 DOOM1.WAD $RPM_BUILD_ROOT%{_datadir}/%{name}/DOOM1.WAD

desktop-file-install --vendor livna                             \
        --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
        %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/


%clean
rm -rf $RPM_BUILD_ROOT


%post
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :


%files
%defattr(-,root,root,-)
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/48x48/apps/*.png
%doc README.TXT doom-shareware-wad-license.txt


%changelog
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
