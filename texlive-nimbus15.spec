Name:		texlive-nimbus15
Version:	58839
Release:	2
Summary:	Support files for Nimbus 2015 Core fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nimbus15
License:	other-free lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nimbus15.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nimbus15.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Nimbus 2015 Core fonts added Greek and Cyrillic glyphs.
This package may be best suited as an add-on to the
comprehensive Times package, providing support for Greek and
Cyrillic. A new intermediate weight of NimbusMono (AKA Courier)
is provided, along with a narrower version which may be useful
for rendering code.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/nimbus15
%{_texmfdistdir}/fonts/vf/public/nimbus15
%{_texmfdistdir}/fonts/type1/public/nimbus15
%{_texmfdistdir}/fonts/tfm/public/nimbus15
%{_texmfdistdir}/fonts/opentype/public/nimbus15
%{_texmfdistdir}/fonts/map/dvips/nimbus15
%{_texmfdistdir}/fonts/enc/dvips/nimbus15
%{_texmfdistdir}/fonts/afm/public/nimbus15
%doc %{_texmfdistdir}/doc/fonts/nimbus15

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
