# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/mentis
# catalog-date 2007-01-09 22:36:10 +0100
# catalog-license lppl
# catalog-version 1.5
Name:		texlive-mentis
Version:	1.5
Release:	4
Summary:	A basis for books to be published by Mentis publishers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mentis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mentis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mentis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mentis.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX class loads scrbook and provides changes necessary
for publishing at Mentis publishers in Paderborn, Germany. It
is not an official Mentis class, merely one developed by an
author in close co-operation with Mentis.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mentis/mentis.cls
%doc %{_texmfdistdir}/doc/latex/mentis/README
%doc %{_texmfdistdir}/doc/latex/mentis/mentis.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mentis/mentis.dtx
%doc %{_texmfdistdir}/source/latex/mentis/mentis.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.5-2
+ Revision: 753852
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.5-1
+ Revision: 718991
- texlive-mentis
- texlive-mentis
- texlive-mentis
- texlive-mentis

