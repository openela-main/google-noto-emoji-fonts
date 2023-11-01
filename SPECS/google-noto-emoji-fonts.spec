%global commit0 aac7ccaa4d1dea4543453b96f7d6fc47066a57ff
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global fontname google-noto-emoji

%if (0%{?fedora} > 25)
%global buildfont 1
%else
%global buildfont 0
%endif


Name:           %{fontname}-fonts
Version:        20200916
Release:        2%{?dist}
Summary:        Google “Noto Emoji” Black-and-White emoji font

# In noto-emoji-fonts source
## noto-emoji code is in ASL 2.0 license
## Emoji fonts are under OFL license
### third_party color-emoji code is in BSD license
### third_party region-flags code is in Public Domain license
# In nototools source
## nototools code is in ASL 2.0 license
### third_party ucd code is in Unicode license
License:        OFL and ASL 2.0
URL:            https://github.com/googlei18n/noto-emoji
Source0:        https://github.com/googlei18n/noto-emoji/archive/%{commit0}.tar.gz#/noto-emoji-%{shortcommit0}.tar.gz
Source2:        %{fontname}.metainfo.xml
Source3:        %{fontname}-color.metainfo.xml

Patch0:         noto-emoji-use-system-pngquant.patch
Patch1:         noto-emoji-build-all-flags.patch
Patch2:         noto-emoji-use-gm.patch

BuildArch:      noarch
BuildRequires:  fontpackages-devel
%if %buildfont
BuildRequires:  fonttools
BuildRequires:  python2-fonttools
BuildRequires:  nototools
BuildRequires:  python2-nototools
BuildRequires:  python2-devel
BuildRequires:  GraphicsMagick
BuildRequires:  pngquant
BuildRequires:  zopfli
BuildRequires:  cairo-devel
%endif

Requires:       fontpackages-filesystem

Obsoletes:      google-noto-color-emoji-fonts < 20150617
Provides:       google-noto-color-emoji-fonts = 20150617

%description
This package provides the Google “Noto Emoji” Black-and-White emoji font.

%package -n     %{fontname}-color-fonts
Summary:        Google “Noto Color Emoji” colored emoji font
Requires:       fontpackages-filesystem
Obsoletes:      google-noto-color-emoji-fonts < 20150617
Provides:       google-noto-color-emoji-fonts = 20150617

%description -n %{fontname}-color-fonts
This package provides the Google “Noto Color Emoji” colored emoji font.

%prep
%autosetup -n noto-emoji-%{commit0}

rm -rf third_party/pngquant

%build
%if %buildfont
# Work around UTF-8
export LANG=C.UTF-8

make %{?_smp_mflags} OPT_CFLAGS="$RPM_OPT_FLAGS"
%endif

%install
install -m 0755 -d %{buildroot}%{_fontdir}

%if %buildfont
# Built by us from the supplied pngs:
install -m 0644 -p NotoColorEmoji.ttf %{buildroot}%{_fontdir}
%else
# Pre-built, and included with the source:
install -m 0644 -p fonts/NotoColorEmoji.ttf %{buildroot}%{_fontdir}
%endif

# Pre-built, and included with the source:
install -m 0644 -p fonts/NotoEmoji-Regular.ttf %{buildroot}%{_fontdir}

mkdir -p %{buildroot}%{_datadir}/appdata
install -m 0644 -p %{SOURCE2} %{buildroot}%{_datadir}/appdata
install -m 0644 -p %{SOURCE3} %{buildroot}%{_datadir}/appdata

%_font_pkg NotoEmoji-Regular.ttf
%license LICENSE
%doc AUTHORS CONTRIBUTING.md CONTRIBUTORS README.md
%{_datadir}/appdata/google-noto-emoji.metainfo.xml

%_font_pkg -n color NotoColorEmoji.ttf
%license LICENSE
%doc AUTHORS CONTRIBUTING.md CONTRIBUTORS README.md
%{_datadir}/appdata/google-noto-emoji-color.metainfo.xml


%changelog
* Tue May 25 2021 Peng Wu <pwu@redhat.com> - 20200916-2
- Rebuild the package
- Resolves: RHBZ#1897541

* Tue May 25 2021 Peng Wu <pwu@redhat.com> - 20200916-1
- Update to Unicode 13.1.0 support
- Resolves: RHBZ#1897541

* Thu Jun 28 2018 Peng Wu <pwu@redhat.com> - 20180508-4
- Resolves: RHBZ#1591712

* Wed Jun 27 2018 Lumír Balhar <lbalhar@redhat.com> - 20180508-3
- Disable build of fonts and rather ship pre-built ones

* Wed May 23 2018 Peng Wu <pwu@redhat.com> - 20180508-2
- Use GraphicsMagick instead of ImageMagick

* Tue May 08 2018 Mike FABIAN <mfabian@redhat.com> - 20180508-1
- Update to upstream snapshot tarball (color emoji font version 2.011)
- Add patch to build all country flags (Resolves: rhbz#1574195)

* Wed Mar 07 2018 Mike FABIAN <mfabian@redhat.com> - 20180307-1
- Update to upstream snapshot tarball (color emoji font version 2.004)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170928-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb  5 2018 Peng Wu <pwu@redhat.com> - 20170928-3
- Use nototools package to build google-noto-emoji-fonts

* Wed Nov  8 2017 Peter Oliver <rpm@mavit.org.uk> - 20170928-2
- Prefer zopflipng to optipng, since it should yield smaller files.
- Use the font we built, rather than the one included with the source.

* Thu Sep 28 2017 Mike FABIAN <mfabian@redhat.com> - 20170828-1
- Update to upstream snapshot tarball
- split black-and-white and color fonts into different sub-packages.

* Mon Aug 28 2017 Mike FABIAN <mfabian@redhat.com> - 20170827-1
- Update to upstream snapshot tarball
- Update color emoji font to version 2.001, new design.
- Contains the new emoji added in Unicode 10.0.0.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170608-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 08 2017 Mike FABIAN <mfabian@redhat.com> - 20170608-1
- Update to upstream snapshot tarball

* Tue May 23 2017 Mike FABIAN <mfabian@redhat.com> - 20170523-1
- Update to upstream snapshot tarball
- This fixes the skin tones of the light/medium light male cook emoji,
  which had been swapped.

* Wed Apr 26 2017 Mike FABIAN <mfabian@redhat.com> - 20170426-1
- Update to upstream snapshot tarball
  (fixes the family emoji sequences:
  kiss: woman, man U+1F469 U+200D U+2764 U+FE0F U+200D U+1F48B U+200D U+1F468
  couple with heart: woman, man U+1F469 U+200D U+2764 U+FE0F U+200D U+1F468)

* Thu Feb 23 2017 Peng Wu <pwu@redhat.com> - 20170223-1
- Update to upstream snapshot tarball

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20160406-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri May  6 2016 Peng Wu <pwu@redhat.com> - 20160406-5
- Avoid to use python setup.py

* Fri Apr 29 2016 Peng Wu <pwu@redhat.com> - 20160406-4
- Replace google-noto-color-emoji-fonts package

* Mon Apr 25 2016 Peng Wu <pwu@redhat.com> - 20160406-3
- Add google-noto-emoji.metainfo.xml

* Wed Apr 20 2016 Peng Wu <pwu@redhat.com> - 20160406-2
- Use system pngquant

* Wed Apr 20 2016 Peng Wu <pwu@redhat.com> - 20160406-1
- Initial packaging
