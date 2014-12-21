%{?_javapackages_macros:%_javapackages_macros}
%global commit bd245c9

Name:           pcfi
Version:        2010.08.09
Release:        8.20111103git%{commit}.2
Summary:        PDF Core Font Information
Group:          Publishing
License:        BSD
URL:            https://github.com/jukka/pcfi
Source0:        https://github.com/jukka/pcfi/tarball/%{commit}/jukka-pcfi-%{commit}.tar.gz
# Originally downloaded from: http://opensource.adobe.com/wiki/display/cmap/License
# This now points to Adobe's sourceforge pages
Source1:        License
BuildArch:      noarch
BuildRequires:  maven-local
Requires:       jpackage-utils


%description
Collection of PDF core font information files downloaded from Adobe's
Developer Center and elsewhere. This collection contains font metrics for the
14 PDF core fonts, CMaps for the PDF CJK fonts and the Adobe Glyph List.   The
files are stored inside the com/adobe/pdf/pcfi directory. See the individual
files for exact licensing information.


%prep
%setup -q -n jukka-pcfi-%{commit}
sed -i 's/\r//' src/main/resources/META-INF/LICENSE.txt
cp %SOURCE1 .


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%doc README.txt src/main/resources/META-INF/LICENSE.txt License


%changelog
* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2010.08.09-8.20111103gitbd245c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Orion Poplawski <orion@cora.nwra.com> - 2010.08.09-7.20111103gitbd245c9
- Use new maven macros to build

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2010.08.09-7.20111103gitbd245c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2010.08.09-6.20111103gitbd245c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2010.08.09-5.20111103gitbd245c9
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2010.08.09-4.20111103gitbd245c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2010.08.09-3.20111103gitbd245c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 3 2011 Orion Poplawski <orion@cora.nwra.com> - 2010.08.09-2.20111103gitbd245c9
- Use github upstream, build with maven
- Drop BuildRoot

* Thu Aug 11 2011 Orion Poplawski <orion@cora.nwra.com> - 2010.08.09-1
- Initial package
