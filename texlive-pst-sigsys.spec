Name:		texlive-pst-sigsys
Version:	21667
Release:	2
Summary:	Support of signal processing-related disciplines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-sigsys
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-sigsys.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-sigsys.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers a collection of useful macros for
disciplines related to signal processing. It defines macros for
plotting a sequence of numbers, drawing the pole-zero diagram
of a system, shading the region of convergence, creating an
adder or a multiplier node, placing a framed node at a given
coordinate, creating an up-sampler or a down-sampler node,
drawing the block diagram of a system, drawing adaptive
systems, sequentially connecting a list of nodes, and
connecting a list of nodes using any node-connecting macro.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-sigsys/pst-sigsys.tex
%{_texmfdistdir}/tex/latex/pst-sigsys/pst-sigsys.sty
%doc %{_texmfdistdir}/doc/generic/pst-sigsys/Changes
%doc %{_texmfdistdir}/doc/generic/pst-sigsys/README
%doc %{_texmfdistdir}/doc/generic/pst-sigsys/pst-sigsys-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-sigsys/pst-sigsys-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-sigsys/pst-sigsys-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
